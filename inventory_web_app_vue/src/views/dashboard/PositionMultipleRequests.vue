<template>
    <div class="page-items">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Position - {{position.name}}</h1>
            </div>



            <div class="column is-fullwidth">
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
                            v-for="(item, index) in items"
                            :key="item.id"
                        >
                            <td>Quantity / Item</td>
                            <td>{{item.quantity}}</td>
                            <td colspan="3">{{itemProperties[index].name}}</td>
                            <td><router-link :to="{name: 'Item', params: {id: item.item}}" class="button is-small is-dark is-fullwidth">Details</router-link></td>
                        </tr>    
                        <tr>
                            <td>Description</td>
                            <td colspan="5">{{position.description}}</td>
                        </tr>
                        <tr>
                            <td>Location</td>
                            <td>{{position.location.building.name}}</td>
                            <td>{{position.location.room.name}}</td>
                            <td>{{position.location.cabinet_number}}</td>
                            <td>{{position.location.box_number}}</td>
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
                            <td colspan="5">{{position.created_by_name}}</td>
                        </tr>
                        <tr>
                            <td>Updated By</td>
                            <td colspan="5">{{position.updated_by_name}}</td>
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
    name: "PositionMultipleRequests",
    data() {
        return{
            position: {},
            items: [],
            itemProperties: [],
        }
    },
    created() {
        this.requests()
    },
    methods: {

        positionRequest() {
            return new Promise ((resolve, reject) => {
                const positionID = this.$route.params.id;

                axios
                .get(`api/v1/positions/${positionID}`)
                .then(response => {
                    this.position = response.data
                    console.log(response.data)
                    resolve()
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                    reject()
                })
            })
        },

        itemRequest() {
            return new Promise ((resolve, reject) => {
                for(let i=0; i < this.position.items.length; i++) {
                    axios
                        .get(`api/v1/position-items/${this.position.items[i]}`)
                        .then(response => {
                            this.items.push(response.data)
                            if (this.items.length == this.position.items.length) {
                                console.log("resolve of getItems()")
                                resolve()
                            }
                        })
                        .catch(error=> {
                            console.log(JSON.stringify(error))
                            reject()
                        })
                }
            })
        },

        itemPropertiesRequest() {
            return new Promise ((resolve, reject) => {
                for(let i=0; i < this.items.length; i++) {
                    axios
                        .get(`api/v1/items/${this.items[i].item}`)
                        .then(response => {
                            this.itemProperties.push(response.data)
                            if (this.itemProperties.length == this.items.length) {
                                resolve()
                            }
                        })
                        .catch(error=> {
                            console.log(JSON.stringify(error))
                            reject()
                        })
                }
            })
        },

        async requests() {
            await this.positionRequest()
            await this.itemRequest()
            await this.itemPropertiesRequest()
            console.log(this.position)
        }
    }
}
</script>