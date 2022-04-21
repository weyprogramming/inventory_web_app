<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Inventory Web App</strong></router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu != showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" :class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <template v-if="$store.state.isAuthenticated">
            <router-link to="/dashboard" class="navbar-item">Dashboard</router-link>
            <router-link to="/items" class="navbar-item">Items</router-link>
            <router-link to="/positions" class="navbar-item">Positions</router-link>


            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/dashboard/my-account" class="button is-light">My Account</router-link>
                <router-link to="/sign-up" class="button is-light">Sign Up Another Member</router-link>
              </div>
            </div>  
          </template>

          <template v-else>
            <router-link to="/" class="navbar-item">Home</router-link>

            <div class="navbar-item">
              <div class="buttons">
                <router-link to="/sign-in" class="button is-success">Log In</router-link>
              </div>
            </div>
          </template>    
        </div>   
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>  

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>
  </div>  
</template>

<script>
import axios from 'axios'

export default{
  data() {
    return {
      showMobileMenu: false,
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token=this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else
       axios.defaults.headers.common['Authorization'] = "Token " + token

  }
}

</script>


<style lang="scss">
@import '../node_modules/bulma';
</style>
