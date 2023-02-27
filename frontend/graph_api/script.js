var options = {
    edges: {
      font: {
        size: 12,
      },
    },
    nodes: {
      shape: "box",
      font: {
        bold: {
          color: "#0077aa",
        },
      },
    },
    physics: {
      enabled: false,
    },
  };

    const api = "http://127.0.0.1:8000/api/jobs/graph/"  // either 3000 for nodejs or 8000 for fastapi

    var myHeaders = new Headers();
    myHeaders.append("accept", "application/json");

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    };
  var network;
  
  function drawGraphAPI() {
        // Reset the graph first
        drawGraph([], [])

        // Get Data from the backend
        fetch(api, requestOptions)
        .then(response => response.json())
        .then(data => {
            drawGraph(data.nodes, data.edges)  // Draw Chart based on API response
        })
        .catch(error => {
            console.log('error', error)
            alert(error)
            return {'response': 'error'}
        });


    }

    function drawGraphMock() {
        var nodes = [
            { id: 1, label: "Management", x: -120, y: -120 },
            {
            id: 2,
            font: { multi: true },
            label:
                "Project Engineer III <b>This</b> is a\n<i>default</i> <b><i>multi-</i>font</b> <code>label</code>",
            x: -40,
            y: -40,
            },
            {
            id: 3,
            font: { multi: "html", size: 20 },
            label:
                "HEAD of Pilot Plant <b>This</b> is an\n<i>html</i> <b><i>multi-</i>font</b> <code>label</code>",
            x: 40,
            y: 40,
            },
            {
            id: 4,
            font: { multi: "md", face: "georgia" },
            label: "Head of Engineering Region II *This* is a\n_markdown_ *_multi-_ font* `label`",
            x: 120,
            y: 120,
            },
        ];
        
        // Describe graph connection / relations of job offers
        var edges = [
            { from: 1, to: 2, label: "Move to" },
            {
            from: 2,
            to: 3,
            font: { multi: true },
            label: "Move to <b>html</b>",
            },
            { from: 3, to: 4, font: { multi: "md" }, label: "Move to *html* to _md_" },
        ];

        drawGraph(nodes, edges)
    }

  function drawGraph(nodes, edges) {
        // Get element where to draw the graph
        var container = document.getElementById("mynetwork");

        var data = {
            nodes: nodes,
            edges: edges,
        };
        // Draw the graph
        network = new vis.Network(container, data, options);
  }