let model;

const modelURL = 'http://localhost:5000/model';

const preview = document.getElementById("preview");
const predictButton = document.getElementById("predict");
const clearButton = document.getElementById("clear");
const numberOfFiles = document.getElementById("number-of-files");
const fileInput = document.getElementById('file');

const predict = async (modelURL) => {}
    let saveFile = () => {
      
        // Get the data from each element on the form.
        const finstat = document.getElementById('finstat');
        const elt = document.getElementById('elt');
        const company = document.getElementById('company');
        const fact value = document.getElementById('factvalue');

        // This variable stores all the data.
        let data = 
            '\r finstat: ' + finstat.value + ' \r\n ' + 
            'elt: ' +elt.value + ' \r\n ' + 
            'company: ' + company.value + ' \r\n ' + 
            'factvalue: ' + factvalue.value;
                  
        // Convert the text to BLOB.
        const textToBLOB = new Blob([data], { type: 'text/plain' });
        const sFileName = 'formData.txt';    // The file to save the data.

        let newLink = document.createElement("a");
        newLink.download = sFileName;

        if (window.webkitURL != null) {
            newLink.href = window.webkitURL.createObjectURL(textToBLOB);
        }
        else {
            newLink.href = window.URL.createObjectURL(textToBLOB);
            newLink.style.display = "none";
            document.body.appendChild(newLink);
        }

        newLink.click(); 
    }