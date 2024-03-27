import { createStore } from "vuex";
import { auth } from "./auth.module";
import { file } from "./file.module";

const store = createStore({
  modules: {
    auth,
    file,
  },
});

export default store;