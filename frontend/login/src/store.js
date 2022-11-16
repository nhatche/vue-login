import { reactive} from "vue"

export const store = reactive({
  at: '',
  changeAt(token) {
    this.at = token
  }
})