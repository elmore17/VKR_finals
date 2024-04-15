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

  register({ login, name, kaf_name, role, password1, password2 }) {
    return api.post('/registration', {
      login,
      name,
      kaf_name,
      role,
      password1,
      password2
    })
      .then(response => {
        return response.data;
      });
  }
}

export default new AuthService();