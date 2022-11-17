import { reactive} from "vue"

export const store = reactive({
  at: '',
  username: '',
  password: '',
  changeAt(token) {
    this.at = token
  }
})