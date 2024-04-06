import CommissionService from "../services/commission.service";
import ppsService from "../services/pps.service";

export const user = {
    namespaced: true,
    actions: {
        adduserscommission({ commit }, data) {
            return CommissionService.adduserscommission(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        deluserscommission({ commit }, data) {
            return CommissionService.deluserscommission(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        settingadmin({ commit }, data) {
            return CommissionService.settingadmin(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        addpps({ commit }, data) {
            return ppsService.addpps(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
        deluserspps({ commit }, data) {
            return ppsService.deluserspps(data).then(
                response => {
                    return Promise.resolve(response);
                },
                error => {
                    return Promise.reject(error);
                }
            );
        },
    }
}