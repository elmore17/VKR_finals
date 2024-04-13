import FileServices from "../services/file.service";

export const file = {
    namespaced: true,
    actions: {
        uploadfile({ commit }, file) {
            return FileServices.uploadfile(file).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        addquestioncommission({ commit }, data) {
            return FileServices.addquestioncommission(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        updateestimatesuser({ commit }, data) {
            return FileServices.updateestimatesuser(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        downloadfile({ commit }, data) {
            return FileServices.downloadfile(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        addquestion({ commit }, data) {
            return FileServices.addquestion(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        adddrafts({ commit }, data) {
            return FileServices.adddrafts(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        deldraft({ commit }, data) {
            return FileServices.deldraft(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        delquestion({ commit }, data) {
            return FileServices.delquestion(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        adddraftfile({ commit }, data) {
            return FileServices.adddraftfile(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        downloadfileZK({ commit }, data) {
            return FileServices.downloadfile(data).then(
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