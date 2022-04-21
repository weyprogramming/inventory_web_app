<template>
    <div class="page-items">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Item - {{item.name}}</h1>

                <router-link v-if="item.id" :to="{ name: 'EditItem', params: { id: item.id }}" class="button is-light mt-4">Edit</router-link>
            </div>



            <div class="column is-half">
                <table class="table is-striped is-bordered is-fullwidth mt-5">
                    <thead>
                        <tr>
                            <th>Item Properties</th>
                            <th>Values</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Name</td>
                            <td>{{item.name}}</td>
                        </tr>
                        <tr>
                            <td>ID</td>
                            <td>{{item.id}}</td>
                        </tr>
                        <tr>
                            <td>Type</td>
                            <td>{{item.item_type}}</td>
                        </tr>
                        <tr>
                            <td>Description</td>
                            <td>{{item.description}}</td>
                        </tr>
                        <tr>
                            <td>Price</td>
                            <td>{{item.price}}</td>
                        </tr>
                        <tr>
                            <td>URL</td>
                            <td>{{item.url}}</td>
                        </tr>
                        <tr>
                            <td>Created At</td>
                            <td>{{item.created_at}}</td>
                        </tr>
                        <tr>
                            <td>Updated At</td>
                            <td>{{item.updated_at}}</td>
                        </tr>
                        <tr>
                            <td>Created By</td>
                            <td>{{item.created_by}}</td>
                        </tr>
                        <tr>
                            <td>Updated By</td>
                            <td>{{item.updated_by}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>         
        </div>
    </div>        
</template>

<script>
import axios from 'axios'

export default {
    name: "Item",
    data() {
        return{
            item: {}
        }
    },
    async mounted() {
        await this.getItem()
    },
    methods: {
        getItem() {
            const itemID = this.$route.params.id

            axios
                .get(`api/v1/items/${itemID}`)
                .then(response => {
                    this.item = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>

