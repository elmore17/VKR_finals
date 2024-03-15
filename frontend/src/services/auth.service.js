import axios from 'axios';

const API_URL = 'http://127.0.0.1:83';

class AuthService {
  login(user) {
    return axios
      .post(API_URL + '/login', {
        login: user.login,
        password: user.password
      })
      .then(response => {
        if (response.data.token) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem('user');
  }

//   register(user) {
//     return axios.post(API_URL + 'signup', {
//       username: user.username,
//       email: user.email,
//       password: user.password
//     });
//   }
}

export default new AuthService();