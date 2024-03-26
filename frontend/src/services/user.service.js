import api from './api';

class UserService {
  getUserBoard() {
    return api.get('/user');
  }
  
  getUserCommission(){
    return api.get('/getuserscommission');
  }
}

export default new UserService();