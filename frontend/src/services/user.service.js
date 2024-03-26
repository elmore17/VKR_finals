import api from './api';

class UserService {
  getUserBoard() {
    return api.get('/user');
  }
}

export default new UserService();