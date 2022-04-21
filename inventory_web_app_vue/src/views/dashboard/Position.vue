<template>
    <div class="page-position">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Position - {{position.name}}</h1>
            </div>

            <div class="column is-12">
                <button class="button is-light" @click="showAddItem= !showAddItem">Add Item to Position</button>
            </div>

            <div class="column is-12" v-if="showAddItem">
                <div class="columns">
                    <div class="column is-5">
                        <div class="control">
                            <input type="text" class="input" placeholder="serach Item..." name="item_query" v-model="itemSearchInput">
                        </div>    
                    </div>
                    <div class="column is-1">
                        <div class="control">
                            <button class="button is-success" @click="searchItem(itemSearchInput)">Search</button>
                        </div>                        
                    </div>
                </div>
                <div class="columns">
                        <div class="card mr-2 mt-2" v-for="item in searchItems" :key="item.id">
                            <div class="card-content">
                                <div class="content">
                                    <table class="table is-bordered">
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
                                            <td>Price</td>
                                            <td>{{item.price}}</td>
                                        </tr>
                                    </table>          
                                </div>
                            </div>
                            
                            <div class="card-footer">
                                <div class="content">
                                    <div class="card-footer-item">
                                        <div class="columns is-fullwidth">
                                            <div class="column is-one-third">
                                                <input class="input is-fullwidth amountInput" type="number" step="1" pattern="\d+" v-model="adding_quantity" placeholder="Amount"/>
                                            </div>
                                            <div class="column is-one-third">
                                                <button class="button is-success is-fullwidth" @click="addItem(item.id)">Add Item</button>
                                            </div>
                                            <div class="column is-one-third">
                                                <router-link class="button is-dark is-fullwidth" :to="{name: 'Item', params: {id: item.id}}">View Details</router-link>
                                            </div>   
                                        </div>  
                                    </div>
                                </div>    
                            </div>            
                        </div>   
                </div>       
            </div>      
    

            <div class="column is-12">
                <table class="table is-striped is-bordered is-fullwidth mt-5">
                    <thead>
                        <tr>
                            <th>Position Properties</th>
                            <th colspan="5">Values</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Name</td>
                            <td colspan="5">{{position.name}}</td>
                        </tr>
                        <tr>
                            <td>ID</td>
                            <td colspan="5">{{position.id}}</td>
                        </tr>
                        <tr
                            v-for="item in position.items"
                            :key="item.id"
                        >
                            <td>Quantity / Item</td>
                            <td>{{item.quantity}}</td>
                            <td colspan="2">{{item.item.name}}</td>
                            <td><button class="button is-danger is-small is-fullwidth" @click="deleteItem(item.id)">Remove</button></td>
                            <td><router-link :to="{name: 'Item', params: {id: item.item.id}}" class="button is-small is-dark is-fullwidth">Details</router-link></td>
                        </tr>    
                        <tr>
                            <td>Description</td>
                            <td colspan="5">{{position.description}}</td>
                        </tr>
                        <tr>
                            <td>Location</td>
                            <td>{{position.location.building.name}}</td>
                            <td>{{position.location.room.name}}</td>
                            <td>Cabinet: {{position.location.cabinet_number}}</td>
                            <td>Box: {{position.location.box_number}}</td>
                            <td><button class="button is-small is-dark is-fullwidth">Details</button></td>
                        </tr>
                        <tr>
                            <td>Created At</td>
                            <td colspan="5">{{position.created_at}}</td>
                        </tr>
                        <tr>
                            <td>Updated At</td>
                            <td colspan="5">{{position.updated_at}}</td>
                        </tr>
                        <tr>
                            <td>Created By</td>
                            <td colspan="5">{{position.created_by}}</td>
                        </tr>
                        <tr>
                            <td>Updated By</td>
                            <td colspan="5">{{position.updated_by}}</td>
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
    name: "Position",
    data() {
        return{
            position: {},
            searchItems: {},
            adding_quantity : "",
            showAddItem : false
        }
    },
    async beforeMount() {
        await this.getPositionDetails()
    },
    methods: {
        getPositionDetails() {
            
            const positionID = this.$route.params.id;

            axios
                .get(`api/v1/position-details/${positionID}`)
                .then(response => {
                    this.position = response.data
                    console.log(response.data)
                    console.log(this.position)
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        deleteItem(itemID) {
            axios
                .delete(`api/v1/position-items/${itemID}`)
                .then(response => {
                    this.getPositionDetails()
                })    
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        searchItem(itemSearchInput) {
            axios
                .get(`api/v1/item-search/`, {
                    params: {
                        'query': itemSearchInput
                    }
                })
                .then(response => {
                    this.searchItems = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        addItem(itemID) {
            const positionID = this.$route.params.id;
            const positionItem = {position: positionID, item: itemID, quantity: this.adding_quantity};

            axios
                .post(`api/v1/position-items/`, positionItem)
                .then(response => {
                    this.getPositionDetails()
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }        
}
</script>

<style>
    .card{
        inline-size: fit-content;
    }
</style>