<template>
  <v-content>
      <v-data-table
        :headers="tableHeader"
        :items="flightData"
        :item-class="customRowClass"
        :single-expand="singleExpand"
        :expanded.sync="expanded"
        item-key="flight_number"
        show-expand
        class="table"
      >
        <!-- <template v-slot:item="{ item }" :class="customRowClass(item)"></template> -->
        <template v-slot:item.time="{ item }">{{ item.departure_time }} - {{ item.arrival_time }}</template>

        <template v-slot:item.avg_price="{ item }">
          
          ${{ item.avg_price }} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <v-icon v-if="item.is_cheap==1" color="yellow" >fas fa-star</v-icon>
          
        </template>

        <template v-slot:item.logo="{ item }"><img :src="changeImgSource(item.flight_number)" style="width:50px;height:50px;"></template>
        

        <template v-slot:item.travel_time="{ item }">
          {{ item.travel_time }}
          <p>{{ item.departure_airport }} - {{ item.arrival_airport }}</p>
        </template>

        <template v-slot:item.one_way>Nonstop</template>

        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Flight Table</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-switch
              v-model="singleExpand"
              label="Single expand"
              class="mt-2"
            ></v-switch>
          </v-toolbar>
        </template>

        <template v-slot:expanded-item="{ item }">
          <td>
            <br></br>
            <v-icon>mdi-seat-legroom-normal</v-icon>Average Legroom
            <br></br>
            <v-icon>mdi-signal-variant</v-icon>Free wifi available
            <br></br>
            <v-icon>mdi-power-plug-outline</v-icon>In-seat power outlet
            <br></br>
            <v-icon>mdi-cellphone-nfc</v-icon>Stream media to your device
          </td>
                   
        </template>
      </v-data-table>

  </v-content>
</template>
<script>
import axios from 'axios';

var url = "http://127.0.0.1:5000";

export default{
  props:['items'],
  data () {
    return {
      flightData: [],
      value:[],
      cityAbv: 
        {"Chicago": "ORD",
        "Los Angeles": "LAX",
        "San Francisco": "SFO",
        },
      singleExpand: false,
      tableHeader: [
        {text: "", align: 'start', sortable: false, value:'logo' },
        {text: "",sortable: false, value:'flight_number'},
        {text: "",sortable: false, value:"time"},
        // {text: "Departure Airport", value:'departure_airport'},
        // {text: "Arrival Airport", value:'arrival_airport'},
        {text: "", sortable: false, value:'travel_time'},
        // {text: "", sortable: false, value:'one_way'},
        {text: "", sortable: false, value:"avg_price"},
        { text: '', value: 'data-table-expand' }
      ],
    }
  },
  created(){
    console.log(this.$route.query.items);
    this.getData();
  },
  methods: {
    getData: function(){
      var aAbv = this.cityAbv[this.$route.query.items.arrivalCity] || "ORD";
      var dAbv = this.cityAbv[this.$route.query.items.departureCity] || "LAX";
      var departDate = this.$route.query.items.departureDate;
      
      axios.get(url+'/api/getFlightsCheaperThanAvg?arrival_airport='+aAbv+'&departure_airport='+dAbv+'&departure_date='+departDate).then(resp => {
          this.getTicketPrice(resp.data);
      });
      
    },
    getTicketPrice:function(fdata){       
      var b = fdata;
      // console.log(fdata);
      for (let i = 0; i < b.length; i++) { 
        var flight_id = b[i]["flight_id"];
        axios.get(url+'/api/getFlightAvgPrice/'+flight_id).then(resp => {
          b[i]["avg_price"] = resp.data[0]["avg_price"].toFixed(2);
          this.flightData.push(b[i])
        });
      }
      
    },
    
    changeImgSource(flightNumber){
      var UALogo = require("../assets/image/UA.jpg")
      var AALogo = require("../assets/image/AA.jpg")
      var NKLogo = require("../assets/image/spirit.jpg")
      var ASLogo = require("../assets/image/AS.jpg")
      var WNLogo = require("../assets/image/WN.jpg")
      var F9Logo = require("../assets/image/F9.jpg")
      var G4Logo = require("../assets/image/G4.jpg")
      var DLLogo = require("../assets/image/DL.jpg")
      var VXLogo = require("../assets/image/VX.jpg")
      var B6Logo = require("../assets/image/B6.jpg")
      var OOLogo = require("../assets/image/OO.jpg")

      var img = ""
      var company = flightNumber.substr(0, 2)
      console.log(company)
      if (company == "UA"){
        img = UALogo
      } else if (company == "AA"){
        img = AALogo
      } else if (company == "NK"){
        img = NKLogo
      } else if (company == "AS"){
        img = ASLogo
      } else if (company == "WN"){
        img = WNLogo
      } else if (company == "F9"){
        img = F9Logo
      } else if (company == "G4"){
        img = G4Logo
      } else if (company == "DL"){
        img = DLLogo
      } else if (company == "VX"){
        img = VXLogo
      } else if (company == "B6"){
        img = B6Logo
      } else if (company == "OO"){
        img = OOLogo
      }

      return img
    },
  },
}
</script>

<style>

.table{
  padding-left: 20%;
  padding-right: 20%;

}

.style-cheap{
  background-color: rgb(215, 215, 44)
}

</style>
