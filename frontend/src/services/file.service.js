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
    getinfofromfile({ id }){
        return api.get('/getinfofromfile?id=' + id)
        .then(response => {
            return response.data;
        })
    }
}

export default new FileServices();