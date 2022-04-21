import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import SignUp from '../views/SignUp.vue'
import SignIn from'../views/SignIn.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Items from '../views/dashboard/Items.vue'
import Item from '../views/dashboard/Item.vue'
import AddItem from '../views/dashboard/AddItem.vue'
import EditItem from '../views/dashboard/EditItem.vue'
import Positions from '../views/dashboard/Positions.vue'
import Position from '../views/dashboard/Position.vue'
import PositionMultipleRequest from '../views/dashboard/PositionMultipleRequests.vue'


import store from '../store'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/sign-in',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/dashboard/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/items',
    name: 'Items',
    component: Items,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/items/:id',
    name: 'Item',
    component: Item,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/items/add',
    name: 'AddItem',
    component: AddItem,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/items/:id/edit',
    name: 'EditItem',
    component: EditItem,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/positions',
    name: 'Positions',
    component: Positions,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/positions/:id',
    name: 'Position',
    component: Position,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/positions/v2/:id',
    name: 'PositionMultipleRequest',
    component: PositionMultipleRequest,
    meta: {
      requireLogin: true
    }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})
export default router
