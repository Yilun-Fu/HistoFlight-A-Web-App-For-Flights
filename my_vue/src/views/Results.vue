<template>
    <v-content>
        <!-- <SearchBar/> -->
        <Data />
    </v-content>
</template>

<script>

import SearchBar from '../components/Search.vue'
import Data from '../components/Data.vue'
export default{
    name: 'Results',
    components:{
        Data,
        SearchBar
    },
    
    
}
</script>