<template>
  <v-content>
      <!-- <div>
        <v-card
          flat
          color="transparent"
        >
          <v-subheader>Min and max default slider</v-subheader>

          <v-card-text>
            <v-row>
              <v-col class="pr-4">
                <v-slider
                  v-model="slider"
                  class="align-center"
                  :max="max"
                  :min="min"
                  hide-details
                >
                  <template v-slot:append>
                    <v-text-field
                      v-model="slider"
                      class="mt-0 pt-0"
                      hide-details
                      single-line
                      type="number"
                      style="width: 60px"
                    ></v-text-field>
                  </template>
                </v-slider>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </div> -->
      <!-- <v-simple-table class="table">
          <template v-slot:default>
              <thead>
              <tr>
                  <th>Flights ({{flightData.length}})</th>
                  <th>Departure City</th>
                  <th>Arrival City</th>
                  <th>Departure Date</th>
                  <th>Departure Time</th>
                  <th>Arrival Date</th>
                  <th>Arrival Time</th>
                  <th>Price</th>
              </tr>
              </thead>
              <tbody>
              <tr
                  v-for="(flight,index) in flightData"
                  :key="index"
              >
                  <td>{{ flight.flight_number }}</td>
                  <td>{{ flight.departure_airport }}</td>
                  <td>{{ flight.arrival_airport }}</td>
                  <td>{{ flight.departure_date }}</td>
                  <td>{{ flight.departure_time }}</td>
                  <td>{{ flight.arrival_date }}</td>
                  <td>{{ flight.arrival_time }}</td>
                  <td>${{ flight.avg_Price }}</td>
              </tr>
              </tbody>
              
          </template>
      </v-simple-table> -->
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
          <!-- <v-spacer></v-spacer> -->
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
        <!-- <template v-slot:expanded-item="{ item }">
          <td>
            <p>More info about {{ item.flight_id }}</p>
          </td>
            <td>
              <v-subheader>Current Price Range</v-subheader>

              <v-card-text>
                <v-slider
                  v-model="f"
                  :tick-labels="ticksLabels"
                  v-bind="{max, tickLabels}"
                  tick-size="0"
                ></v-slider>
              </v-card-text>
            </td> -->
            <!-- <v-slider
              v-model="ex3.val"
              :label="ex3.label"
              :thumb-color="ex3.color"
              thumb-label="always"
              :tick-labels="tickLabels"
            ></v-slider> -->
          
        <!-- </template> -->
        <template v-slot:expanded-item="{ item }">
          <td>
            <!-- <v-range-slider
              :tick-labels="flightTicksLabels"
              :value="[0, 1]"
              min="0"
              max="1"
              ticks="always"
              vertical
              disabled
                            
            >
               <template v-slot:thumb-label="props">
                <v-icon dark>
                  {{ flightTicksLabels(props.value) }}
                </v-icon>
              </template> -->
            <!-- </v-range-slider> -->
            {{item.flight_number}}
            <v-icon>fas fa signal-variant</v-icon>Free wifi available
          </td>
          
          <!-- <td>
              <v-subheader>Current Price Range</v-subheader>

              <v-card-text>
                <v-slider
                  v-model="f"
                  :tick-labels="ticksLabels"
                  v-bind="{max, tickLabels}"
                  tick-size="0"
                ></v-slider>
              </v-card-text>
          </td> -->
          <!-- <td>
            {{item.flight_number}}
          </td> -->
          
        </template>
      </v-data-table>
      <v-card
        class="mx-auto text-center"
        color="cyan"
        dark
        max-width="800"
      >
        <v-card-text>
          <v-sheet color="rgba(0, 0, 0, .12)">
            <v-sparkline
              :value="value"
              color="white"
              height="100"
              padding="14"
              stroke-linecap="round"
              smooth
              label-size="4"
              auto-line-width="true"
            >
              <template v-slot:label="item">
                ${{ item.value }}
              </template>
            </v-sparkline>
          </v-sheet>
        </v-card-text>

        <v-card-text>
          <div class="text-h4 font-weight-thin">
            Range of Flight Prices
          </div>
        </v-card-text>

        <v-divider></v-divider>

        <!-- <v-card-actions class="justify-center">
          <v-btn
            block
            text
          >
            Go to Report
          </v-btn>
        </v-card-actions> --> 
      </v-card> 
      
      <line-chart :chart-data="datacollection"></line-chart>

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
      // UALogo: require("../assets/image/UA.jpg"),
      // f:1,
      // ex3: { label: 'thumb-color', val: 50, color: 'red' },
      value:[],
      cityAbv: 
        {"Chicago": "ORD",
        "Los Angeles": "LAX",
        "San Francisco": "SFO",
        },
      // min: -50,
      max: 2,
      // slider: 40,
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
      ticksLabels:[
        '0',
        '163.5',
        '200',
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
      var set = new Set();
      console.log(fdata);
      for (let i = 0; i < b.length; i++) { 
        var flight_id = b[i]["flight_id"];
        axios.get(url+'/api/getFlightAvgPrice/'+flight_id).then(resp => {
          b[i]["avg_price"] = resp.data[0]["avg_price"].toFixed(2);
          // b[i]["is_cheap"] = 1
          this.flightData.push(b[i])
          set.add(parseFloat(resp.data[0]["avg_price"].toFixed(2)))
          console.log(set)
          this.value = Array.from(set).sort(function(a, b){return a - b});
          console.log(this.value)

          this.setDataCollection(b)
        });
      }
      
    },
    setDataCollection:function(fdata){
      var flabel = [];
      var pricedata = [];
      // {
      //   data: [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478],
      //     label: "Africa",
      //     borderColor: "#3e95cd",
      //     fill: false
      // }
      for (let i = 0; i<this.flightData.length;i++){
        flabel.push(this.flightData[i]["flight_number"])
        pricedata.push(parseFloat(this.flightData[i]["avg_price"]))
      }
      this.datacollection = {
        labels: flabel,
        datasets: [{
          data: pricedata,
          label: "",
          borderColor: "#3e95cd",
          fill: false
        }]
      }
    },
    changeImgSource(flightNumber){
      var UALogo = require("../assets/image/UA.jpg")
      var AALogo = require("../assets/image/AA.jpg")
      var NKLogo = require("../assets/image/spirit.jpg")
      // var ASLogo = require("../assets/image/AS.jpg")
      // var WNLogo = require("../assets/image/WN.jpg")

      var img = ""
      var company = flightNumber.substr(0, 2)
      console.log(company)
      if (company == "UA"){
        img = UALogo
      } else if (company == "AA"){
        img = AALogo
      } else if (company == "NK"){
        img = NKLogo
      }
      // } else if (company == "AS"){
      //   img = ASLogo
      // } else if (company == "WN"){
      //   img = WNLogo
      // }

      return img
    },
    // customRowClass(item) {
    //   if (item.is_cheap == 1) return 'style-cheap';

    // }
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
