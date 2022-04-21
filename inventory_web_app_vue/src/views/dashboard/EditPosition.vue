<template>
     <div class="page-edit-position">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit - {{item.name}}</h1>
            </div>

            <div class="column is-12">
                <div class="select">
                    <select name="type" v-model="item.item_type">
                        <option selected value="">- Select Type -</option>
                        <option value="tool">Tool</option>
                        <option value="consumable">Consumable</option> 
                    </select>
                </div>
            </div>       

                <div class="columns is-vcentered mt-3">
                    <div class="column is-half">
                        <div class="field">
                            <label>Name</label>

                            <div class="control">
                                <input type="text" name="name" class="input" v-model="item.name">
                            </div>
                        </div>
                        <div class="field">
                            <label>Price</label>

                            <div class="control">
                                <input type="text" name="name" class="input" v-model="item.price">
                            </div>
                        </div>
                        <div class="field">
                            <label>URL</label>

                            <div class="control">
                                <input type="text" name="name" class="input" v-model="item.url">
                            </div>
                        </div>
                    </div>
                    
                    <div class="column is-half">
                        <div class="field">
                            <label>Description</label>

                            <div class="control">
                                <textarea type=text name="description" class="textarea" rows="7" v-model="item.description"></textarea>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-12">
                    <div class="field">
                        <div class="control">
                            <button class="button is-success" @click="submitForm">Save Changes</button>
                        </div>
                    </div>
                </div>
        </div>
    </div>    
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'EditPosition',
    data() {
        return {
            item: {}
        }
    },
    mounted() {
        this.getItem()
    },
    methods: {
        getItem() {
            const positionID = this.$route.params.id

            axios
                .get(`api/v1/items/${itemID}`)
                .then(response => {
                    this.item = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        submitForm() {
            const itemID = this.$route.params.id

            axios
                .patch(`/api/v1/items/${itemID}/`, this.item)
                .then(response => {
                    toast({
                        message: 'The Changes have been made sucessfully',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    })
                    this.$router.push('/items/')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>