<template>
    <div class="page-items">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Positions</h1>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth is-striped">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Position</th>
                            <th>Items</th>
                            <th>Location</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                        <tr
                            v-for="position in positions"
                            :key ="position.id"
                        >
                            <td>{{position.id}}</td>
                            <td>{{position.name}}</td>
                            <td>{{position.items}}</td>
                            <td>{{position.location}}</td>
                            <td>
                                <div class="buttons">
                                    <button class="button is-light">Details</button>
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
    name: "Positions",
    data() {
        return {
            positions: []
        }
    },
    mounted() {
        this.getPositions()
    },
    methods: {
        getPositions() {
            axios
                .get('api/v1/positions/')
                .then(response => {
                    for (let i = 0; i < response.data.length; i++) {
                        this.positions.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>