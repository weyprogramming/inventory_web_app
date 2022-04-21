<template>
    <div class="page-items">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Items</h1>
                <router-link :to="{ name: 'AddItem'}" class="button is-light mt-4">Add Item</router-link>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth is-striped">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Item</th>
                            <th>Type</th>
                            <th>Price</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                        <tr
                            v-for="item in items"
                            :key ="item.id"
                        >
                            <td>{{item.id}}</td>
                            <td>{{item.name}}</td>
                            <td>{{item.item_type}}</td>
                            <td>{{item.price}}</td>
                            <td>
                                <div class="buttons">
                                    <router-link :to="{name: 'Item', params: {id: item.id}}" class="button is-light">Details</router-link>
                                    <router-link v-if="item.id" :to="{ name: 'EditItem', params: { id: item.id }}" class="button is-light">Edit</router-link>
                                </div>    
                            </td>  
                        </tr>
                    <tbody>

                    </tbody>
                </table>
            </div>            
        </div>
    </div>         
</template>

<script>
import axios from 'axios'

export default {
    name: "Items",
    data() {
        return {
            items: []
        }
    },
    mounted() {
        this.getItems()
    },
    methods: {
        getItems() {
            axios
                .get('api/v1/items/')
                .then(response => {
                    for (let i = 0; i < response.data.length; i++) {
                        this.items.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>