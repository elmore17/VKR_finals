import { createStore } from "vuex";
import { auth } from "./auth.module";
import { file } from "./file.module";
import { user } from "./user.module";

const store = createStore({
  modules: {
    auth,
    file,
    user,
  },
});

export default store;