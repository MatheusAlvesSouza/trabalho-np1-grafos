var global_nodes;

// Pega todos nós no input_nodes
const getNodes = () => {
  const input = document.getElementById("input_nodes").value; // Pega o input
  const nodes = input.split(' '); // Quebra por espaço

  for (let i = 0; i < nodes.length; i++) {
    if (nodes[i] == "") {
      continue;
    }

    nodes[i] = {
      'id': i,
      'node': nodes[i],
      'links': []
    };
  }

  createInputLinks(nodes);
}

// Cria todos os inputs com os links a serem inputados
const createInputLinks = (nodes) => {

  //Limpando o Array
  nodes = removeItem(nodes, "");
  nodes = removeItem(nodes, " ");
  global_nodes = nodes;

  //ONDE O ITEM SERÁ INPUTADO
  var destino = document.getElementById('container_adjacencias');
  
  //ADICIONANDO AO DESTINO
  destino.innerHTML = "";

  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i];

    if (!node.node) {
      nodes.
      continue;
    }

    let label = document.createElement("LABEL");
    label.innerHTML = "Adjacências de " + node.node + ": ";
    destino.appendChild(label);
    
    let input = document.createElement("INPUT");
    input.type = "text";
    input.name = "adjacencias";
    input.class = "adjancencias";
    input.dataset.id_node = node.id;
    input.onkeydown = createAdjacencias;
    destino.appendChild(input);
    
    let br = document.createElement("BR");
    destino.appendChild(br);
  }
}

// Pega todos os inputs de adjacencias
const createAdjacencias = () => {
  const nodes = global_nodes;
  const inputs = document.getElementsByName("adjacencias");

  for (let i = 0; i < inputs.length; i++)
  {
    const input = inputs[i];
    const id = input.dataset.id_node;
    let adjacencias = input.value.split(' ');

    adjacencias = removeItem(adjacencias, "");
    adjacencias = removeItem(adjacencias, " ");

    let adjacencias_filtradas = adjacencias;
    for (let x = 0; x < adjacencias.length; x++)
    {
       //verifica se existe um no com o input inserido
      let teste = nodes.filter( nodes => nodes.node == adjacencias[x] );

      // Se o retorno da lista for 0 exclui o item com esse nome
      if (teste.length == 0) {
        adjacencias_filtradas = removeItem(adjacencias_filtradas, adjacencias[x]);
      }
    }

    nodes[id].links = adjacencias_filtradas; // Seta todas as adjacencias encontradas
  }

  createList(nodes);
}

// Cria a lista
const createList = (nodes) => {
  let rows = [];
  for( let i = 0; i < nodes.length; i++)
  {
    const row = nodes[i].node + ": " + nodes[i].links;
    rows.push(row);
  }
}

// Cria a matriz
const createMatriz = (nodes) => {
  let matriz = new Array();
}

function removeItem(array, element) {
  return array.filter(el => el !== element);
}