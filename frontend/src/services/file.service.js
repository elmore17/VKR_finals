import api from "./api";


class FileServices {
    uploadfile({ file }) {
        return api.post('/uploadfile', {
            file
        },
            {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(response => {
                return response.data;
            });
    }
    getfilelist() {
        return api.get('/uploadfile');
    }
    getestimates() {
        return api.get('/get_estimatesvkr');
    }
    getestimatesdip() {
        return api.get('/get_estimatesdip');
    }
    getnamedrafts() {
        return api.get('/namedrafts');
    }
    getstateuserbe({ id }) {
        return api.get('/updatestateuser?id=' + id).then(
            response => {
                return response.data;
            }
        );
    }
    getinfofromfile({ id }) {
        return api.get('/getinfofromfile?id=' + id)
            .then(response => {
                return response.data;
            });
    }
    getdatefromfile({ id }) {
        return api.get('/getdatefromfile?id=' + id)
            .then(response => {
                return response.data;
            });
    }
    getquestioncommission({ id }) {
        return api.get('/questioncommission?id=' + id)
            .then(response => {
                return response.data;
            });
    }
    addquestioncommission({ idUserCommission, idStudent, textQuestion }) {
        return api.post('/questioncommission', {
            idUserCommission,
            idStudent,
            textQuestion
        }).then(
            response => {
                return response.data;
            }
        );
    }
    getestimatesuser({ id }) {
        return api.get('/estimates?id=' + id)
            .then(response => {
                return response.data;
            });
    }
    updateestimatesuser({ student_id, score_gw, score_g }) {
        return api.post('/estimates', {
            student_id,
            score_gw,
            score_g
        }).then(
            response => {
                return response.data;
            }
        )
    }
    updatestateuser({ student_id, state }) {
        return api.post('/updatestateuser', {
            student_id,
            state
        }).then(
            response => {
                return response.data;
            }
        )
    }
    checkstateuser({ id }) {
        return api.get('/checkstatus?id=' + id)
            .then(response => {
                return response.data;
            });
    }
    downloadfile({ userbd, fileID, date, namepred, userscommission }) {
        return api.post('/downloadfile', {
            userbd,
            fileID,
            date,
            namepred,
            userscommission
        }).then(
            response => {
                return response.data;
            }
        )
    }
    addquestion({ month, question }) {
        return api.post('/addquestion', {
            month,
            question
        }).then(
            response => {
                return response.data;
            }
        );
    }
    getquestion() {
        return api.get('/addquestion');
    }
    delquestion({ id }) {
        return api.post('/delquestion', {
            id
        }).then(
            response => {
                return response.data;
            }
        );
    }
    adddrafts({ id_name, text_draft }) {
        return api.post('/adddrafts', {
            id_name,
            text_draft
        }).then(
            response => {
                return response.data;
            }
        );
    }
    getdrafts() {
        return api.get('/adddrafts');
    }
    deldraft({ id }) {
        return api.post('/deldraft', {
            id
        }).then(
            response => {
                return response.data;
            }
        );
    }
    adddraftfile({ data, pred, adminuser, file_name, json, checkedItems }) {
        return api.post('/adddraftfile', {
            data,
            pred,
            adminuser,
            file_name,
            json,
            checkedItems
        }).then(
            response => {
                return response.data;
            }
        );
    }
    getdraftsfile() {
        return api.get('/adddraftfile');
    }
    getroleandmoreinfo() {
        return api.get('/draftsrole');
    }
    getdraftsfileinfo({ id }) {
        return api.get('/draftsfileinfo?id=' + id)
            .then(response => {
                return response.data;
            });
    }
    downloadfileZK({ data, pred, json, adminuser, pps, checkedItems, fileId }) {
        return api.post('/downloadfileZK', {
            data,
            pred,
            json,
            adminuser,
            pps,
            checkedItems,
            fileId
        }).then(
            response => {
                return response.data;
            });
    }
    updateDataQuestion({ old_text, new_text }) {
        return api.post('/updatedataquestion', {
            old_text,
            new_text
        }).then(
            response => {
                return response.data;
            });
    }
    delquestioncommission({ name, data }) {
        return api.post('/delquestioncommission', {
            name,
            data
        }).then(
            response => {
                return response.data;
            });
    }
}

export default new FileServices();