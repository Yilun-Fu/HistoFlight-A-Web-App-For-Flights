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
          :single-expand="singleExpand"
          :expanded.sync="expanded"
          item-key="flight_number"
          show-expand
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Expandable Table</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-switch
                v-model="singleExpand"
                label="Single expand"
                class="mt-2"
              ></v-switch>
            </v-toolbar>
          </template>
          <template v-slot:expanded-item="{ headers, item }">
            <td :colspan="headers.length">
              More info about {{ item.flight_id }}
              <v-subheader>Current Price Range</v-subheader>

              <v-card-text>
                <v-slider
                  v-model="f"
                  :tick-labels="ticksLabels"
                  v-bind="{max, tickLabels}"
                  tick-size="0"
                ></v-slider>
              </v-card-text>
              
              <!-- <v-slider
                v-model="ex3.val"
                :label="ex3.label"
                :thumb-color="ex3.color"
                thumb-label="always"
                :tick-labels="tickLabels"
              ></v-slider> -->

            </td>
            
          </template>
        </v-data-table>
    </v-content>
</template>
<script>
import axios from 'axios'

var url = "http://127.0.0.1:5000";

export default{
    props:['items'],
    data () {
      return {
        // flightData: [],
        f:1,
        ex3: { label: 'thumb-color', val: 50, color: 'red' },
        flightData: [
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "23:59:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "21:21:00",
        "flight_id": "0046a1e4b8a1c5bccc46c1bfaa7814401724122f4e4d3afd74bbda81bb87f1d6",
        "flight_number": "UA 1963",
        "travel_time": "4:38:00",
        "avg_price": "163.2"
    },
    {
        "airline_code": "AA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "15:55:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "13:13:00",
        "flight_id": "01b1003dda96998d68117e9b60ca82341c093d5c517d226b03a5ad667c437c5c",
        "flight_number": "AA 2431",
        "travel_time": "4:42:00"
    },
    {
        "airline_code": "NK",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "18:28:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "16:00:00",
        "flight_id": "08aab6fb0890185219b0d0c2c81473f4e406176953f33c820c52430442c3ddfb",
        "flight_number": "NK 644",
        "travel_time": "4:28:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "18:10:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "15:45:00",
        "flight_id": "16505b80060a5aa3c7e5f5f30e88e2009adc53b6865a4ab883269f8ab27aea87",
        "flight_number": "UA 2095",
        "travel_time": "4:25:00"
    },
    {
        "airline_code": "AA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "9:06:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "6:40:00",
        "flight_id": "2d198f9b18a39fb9b3bd5ad417da5cb622924f005bc840d363ca2dfec9f08d5a",
        "flight_number": "AA 669",
        "travel_time": "4:26:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "13:09:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "10:35:00",
        "flight_id": "43f8b82c4d449c11483884c3043cee8f5a36e8d67db021746d9ffe446ddc3cb5",
        "flight_number": "UA 1147",
        "travel_time": "4:34:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "10:10:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "7:50:00",
        "flight_id": "571484e9034c68ee857df0b39d15669601270fcc83391e23b72a3894187dc52f",
        "flight_number": "UA 2105",
        "travel_time": "4:20:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "11:32:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "9:05:00",
        "flight_id": "67853c5941188f74cc43380f06fb9d81cb59a1e39109c5fb4604272f9c6ecd61",
        "flight_number": "UA 2142",
        "travel_time": "4:27:00"
    },
    {
        "airline_code": "AA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "12:31:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "9:52:00",
        "flight_id": "6f30132af558a07559490b2cf32365cd3bda78e4da82c0ece0500b2f95c24a35",
        "flight_number": "AA 2184",
        "travel_time": "4:39:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "20:44:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "18:08:00",
        "flight_id": "788e6bd26072c58a1561879375fd7629b25c42c2b5ccd4368f00d1a6be9acbd6",
        "flight_number": "UA 1067",
        "travel_time": "4:36:00"
    },
    {
        "airline_code": "AA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "16:39:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "14:00:00",
        "flight_id": "7b263ce5dd76e7fecfb29717ec60186ea69b4dc2a6599a80bea4790f150c5873",
        "flight_number": "AA 2968",
        "travel_time": "4:39:00"
    },
    {
        "airline_code": "NK",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "7:33:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "5:05:00",
        "flight_id": "7f117c3c7204fffb380cd34311aaeba3706db19510e581454f9cbae98f63b322",
        "flight_number": "NK 1359",
        "travel_time": "4:28:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "22:33:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "19:57:00",
        "flight_id": "a3fd4dbb03f0356bcebdbda3d17c62fa63b85b8fd8170a6cd145b88b3a3f9734",
        "flight_number": "UA 2649",
        "travel_time": "4:36:00"
    },
    {
        "airline_code": "AA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "17:42:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "15:15:00",
        "flight_id": "b79343e157a2ee6de4907234d1ce80dc92008cfee4af28f8d13be6ed1b001b9c",
        "flight_number": "AA 1375",
        "travel_time": "4:27:00"
    },
    {
        "airline_code": "NK",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-11",
        "arrival_time": "0:28:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "21:59:00",
        "flight_id": "cddee1485ba78d9235eb2eb1a49e82067f70f43501475b250116574d395354e1",
        "flight_number": "NK 1024",
        "travel_time": "4:29:00"
    },
    {
        "airline_code": "AA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "10:49:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "8:19:00",
        "flight_id": "d25c2902cba36a12b09f94606727f18ea25b8578cd11683c902ecc525d6ff9d4",
        "flight_number": "AA 2882",
        "travel_time": "4:30:00"
    },
    {
        "airline_code": "AA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "19:33:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "17:05:00",
        "flight_id": "d3512129bc239f4b0ac2cbaba9c83a9c58fb6bcbb4e815571841d3ed116b270e",
        "flight_number": "AA 1384",
        "travel_time": "4:28:00"
    },
    {
        "airline_code": "AA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "22:19:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "19:45:00",
        "flight_id": "d4a745b397847ac05b958be484502839364b53f2aa83103431d15fa499855c2f",
        "flight_number": "AA 374",
        "travel_time": "4:34:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "16:55:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "14:22:00",
        "flight_id": "e6c4338523bbaaf834a645ee2eaa76d2537f25add1eb56dc84f080ace75a85f0",
        "flight_number": "UA 2451",
        "travel_time": "4:33:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "15:19:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "12:46:00",
        "flight_id": "e8df03b7a490dbdf846b3517e15e0fb3e919d7de12aea7c0359ccfeaf90d797e",
        "flight_number": "UA 1139",
        "travel_time": "4:33:00"
    },
    {
        "airline_code": "UA",
        "arrival_airport": "LAX",
        "arrival_date": "2022-11-10",
        "arrival_time": "8:35:00",
        "departure_airport": "ORD",
        "departure_date": "2022-11-10",
        "departure_time": "6:02:00",
        "flight_id": "f78aaee89baddaf901bdfdf7bd828f34eae50b247aced0f09b7b238ca3d7f7f9",
        "flight_number": "UA 2050",
        "travel_time": "4:33:00"
    }
],
        cityAbv: 
          {"Chicago": "ORD",
          "Los Angeles": "LAX",
          "San Francisco": "SFO",
          },
        ex3: { label: 'thumb-color', val: 50, color: 'red' },
        // min: -50,
        max: 2,
        // slider: 40,
        singleExpand: false,
        tableHeader: [
          {text: "Flight Number",align: 'start', value:'flight_number'},
          {text: "Departure Airport", value:'departure_airport'},
          {text: "Arrival Airport", value:'arrival_airport'},
          {text: "Arrival Time", value:'arrival_time'},
          {text: "Departure Time", value:'departure_time'},
          {text: "Travel Time", value:'travel_time'}
        ],
        ticksLabels:[
          '0',
          '163.5',
          '200',
        ]
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
        if (this.$route.query.items.avgPrice == true){
            axios.get(url+'/api/getFlightsCheaperThanAvg?arrival_airport='+aAbv+'&departure_airport='+dAbv+'&departure_date='+departDate).then(resp => {
              this.getTicketPrice(resp.data);
          });
        }else{
          axios.get(url+'/api/flight?arrival_airport='+aAbv+'&departure_airport='+dAbv+'&departure_date='+departDate).then(resp => {
            this.getTicketPrice(resp.data);
          });
        }
      },
      getTicketPrice:function(fdata){       
        var b = fdata;
        console.log(fdata);
        for (let i = 0; i < b.length; i++) {
          var flight_id = b[i]["flight_id"];
          axios.get(url+'/api/getFlightAvgPrice/'+flight_id).then(resp => {
            b[i]["avg_Price"] = resp.data[0]["avg_price"].toFixed(2);
            this.flightData.push(b[i])
          });
        }
      },
    },
}
</script>

<style>

.table{
    padding-left: 20%;
    padding-right: 20%;

}

</style>
