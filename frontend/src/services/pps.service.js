import api from "./api";

class PPS {
    addpps({ name, departament, post, academic_title, degree }) {
        return api.post('/addpps', {
            name,
            departament,
            post,
            academic_title,
            degree
        }).then(
            response => {
                return response.data;
            }
        );
    }
    getpps(){
        return api.get('/addpps');
    }
    deluserspps({ id }) {
        return api.post('/deluserpps', {
            id
        }).then(
            response => {
                return response.data;
            }
        )
    }
}

export default new PPS;