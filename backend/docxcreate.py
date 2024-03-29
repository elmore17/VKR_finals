import json
from docx import Document
from docxtpl import DocxTemplate
import locale
from datetime import datetime
import psycopg2

# Устанавливаем русскую локаль
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

def get_db_connection():
    return psycopg2.connect(database="kisprod", user="postgres", password="", host="localhost", port="5432")

def read_docx(docx_path, items_per_subarray=142):
    doc = Document(docx_path)
    all_text_list = []

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                text = cell.text.strip()
                if text:
                    all_text_list.append(text)

    divided_data = [all_text_list[i:i + items_per_subarray] for i in range(0, len(all_text_list), items_per_subarray)]

    return divided_data

# Вставка данных в шаблон
def create_draft(data, output_docx_path, namepred, userscommission):
    doc = DocxTemplate('shablon.docx')
    
    combined_doc = Document()
    
    for item in data:
        date_obj = datetime.combine(item[0], datetime.min.time())
        day_name = date_obj.strftime('%d')
        month_name = date_obj.strftime('%B')
        year_name = date_obj.strftime('%Y')
        context = {
            'day': day_name,
            'mouth': month_name,
            'year': year_name,
            'napravlenie': item[1],
            'predgos': namepred,
            'studentA': item[3],
            'title': item[4],
            'nauchruc': item[5],
            'rang': item[6],
            'student': item[3],
            'predgossokr': namepred,
        }

        for i, usercommission in enumerate(userscommission, start=1):
            context['namegoskom' + str(i)] = usercommission['user_name']

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('select uc.user_name, pi2.text_issues from protection_issues pi2, users_commission uc where pi2.id_student = %s and pi2.id_user_commission = uc.id_user', (item[2],))
            questions = cursor.fetchall()
            questions_dict = {}
            for question in questions:
                name = question[0]
                question = question[1]
                if name in questions_dict:
                    questions_dict[name].append(question)
                else:
                    questions_dict[name] = [question]
            questions = [{"name": name, "question": questions_dict[name]} for name in questions_dict]
            for i in range(len(questions)):
                context['question' + str(i+1)] = questions[i]['name']+ ' ' + str(' '.join(questions[i]['question']))

            cursor.execute('select ee.name, ee.text from assessments a, existing_estimates ee where a.id_student = %s and a.score_graduate_work = ee.id', (item[2],))
            score = cursor.fetchone()
            context['score'] = score[0]
            context['haracteransver1'] = score[1]
                    
                     
            
        doc.render(context)

        for element in doc.element.body:
            combined_doc.element.body.append(element)

    combined_doc.save(output_docx_path)