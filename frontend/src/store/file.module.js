import FileServices from "../services/file.service";

const user = JSON.parse(localStorage.getItem('user'));
const initialState = user
  ? { status: { loggedIn: true }, user }
  : { status: { loggedIn: false }, user: null };

export const file = {
    namespaced: true,
    actions:{
        uploadfile({ commit }, file){
            return FileServices.uploadfile(file).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        }
    }
};