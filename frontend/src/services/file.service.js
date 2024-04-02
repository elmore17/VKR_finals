import api from "./api";


class FileServices{
    uploadfile({ file }){
        return api.post('/uploadfile',{
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
    getfilelist(){
        return api.get('/uploadfile');
    }
    getestimates(){
        return api.get('/get_estimatesvkr');
    }
    getestimatesdip(){
        return api.get('/get_estimatesdip');
    }
    getinfofromfile({ id }){
        return api.get('/getinfofromfile?id=' + id)
        .then(response => {
            return response.data;
        });
    }
    getdatefromfile({ id }){
        return api.get('/getdatefromfile?id=' + id)
        .then(response => {
            return response.data;
        });
    }
    getquestioncommission({ id }){
        return api.get('/questioncommission?id=' + id)
        .then(response =>{
            return response.data;
        });
    }
    addquestioncommission({ idUserCommission, idStudent, textQuestion }){
        return api.post('/questioncommission',{
            idUserCommission,
            idStudent,
            textQuestion
        }).then(
            response => {
                return response.data;
            }
        );
    }
    getestimatesuser({ id }){
        return api.get('/estimates?id=' + id)
        .then(response => {
            return response.data;
        });
    }
    updateestimatesuser({student_id, score_gw, score_g}){
        return api.post('/estimates',{
            student_id,
            score_gw,
            score_g
        }).then(
            response => {
                return response.data;
            }
        )
    }
    checkstateuser({ id }){
        return api.get('/checkstatus?id=' + id)
        .then(response => {
            return response.data;
        });
    }
    downloadfile({userbd, fileID, date, namepred, userscommission}){
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
}

export default new FileServices();