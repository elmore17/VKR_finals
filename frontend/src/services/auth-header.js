export default function authHeader() {
    let user = JSON.parse(localStorage.getItem('user'));
  
    if (user && user.token) {
      // for app.py  back-end
      return { 'x-access-token': user.token };
    } else {
      return {};
    }
}