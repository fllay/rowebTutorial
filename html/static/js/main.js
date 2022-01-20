import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
 
Vue.use(VueAxios, axios)

Vue.use(BootstrapVue)
//require('./eventemitter2.min.js')
//require('./jquery-3.2.1.min.js')
//require('./easeljs.min.js')
//require('./nav2d.min.js')
//require('./ros2d.js')

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
