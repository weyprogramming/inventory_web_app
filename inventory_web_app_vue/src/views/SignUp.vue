<template>
    <div class="page-signup">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign Up</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>E-Mail</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>First Name</label>
                        <div class="control">
                            <input type="text" name="first_name" class="input" v-model="first_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Last Name</label>
                        <div class="control">
                            <input type="text" name="last_name" class="input" v-model="last_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Department</label>
                        <div class="control">
                            <input type="text" name="department" class="input" v-model="department">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p
                            v-for="error in errors"
                            v-bind:key = "error"
                        >
                            {{error}}
                        </p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Sign Up</button>
                        </div>
                    </div>        
                </form>
            </div>
        </div>
    </div>                
</template>

<script>
import axios from 'axios'
    export default {
        name: "SignUp",
        data() {
            return {
                email: '',
                first_name: '',
                last_name: '',
                department: '',
                password: '',
                errors: []
            }
        },
        methods: {
            submitForm(e) {
                const formData = {
                    email: this.email,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    department: this.department,
                    password: this.password,
                }

                axios
                    .post("api/v1/users/", formData)
                    .then(response => {
                        console.log(response)

                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }

                        console.log(JSON.stringify(error.response.data))
                    } else if (error.message) {
                        console.log(JSON.stringify(error.message))
                    } else {
                        console.log(JSON.stringify(error))
                    }
                    })
            }
        }
    }
</script>