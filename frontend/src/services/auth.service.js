import api from "./api";
import TokenService from "./token.service";

class AuthService {
  login({ login, password }) {
    return api
      .post('/login', {
        login,
        password
      })
      .then(response => {
        if (response.data.token) {
          TokenService.setUser(response.data);
        }

        return response.data;
      });
  }

  logout() {
    TokenService.removeUser();
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