import api from "./api";

class CommissionService{
    adduserscommission({fullname, post, date_start, date_end}){
        return api.post('/adduserscommission', {
            fullname,
            post,
            date_start,
            date_end
        }).then(
            response => {
                return response.data;
            }
        );
    }
    deluserscommission({id}){
        return api.post('/delusercommission', {
            id
        }).then(
            response => {
                return response.data;
            }
        )
    }
    settingadmin({newFIO, idAdmin}){
        return api.post('/settingadmin',{
            newFIO,
            idAdmin
        }).then(
            response => {
                return response.data;
            }
        );
    }
}

export default new CommissionService();