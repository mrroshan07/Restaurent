function show(id){
    if(id=='Nonveg'){
        document.getElementById(id).classList.remove('hide');
        document.getElementById('Vegetarien').classList.add('hide');
        document.getElementById('Bewarages').classList.add('hide');
    }
    else if(id=='Vegetarien'){
        document.getElementById(id).classList.remove('hide');
        document.getElementById('Nonveg').classList.add('hide');
        document.getElementById('Bewarages').classList.add('hide');    
    }
    else if(id=='Bewarages'){
        document.getElementById(id).classList.remove('hide');
        document.getElementById('Nonveg').classList.add('hide');
        document.getElementById('Vegetarien').classList.add('hide');    
    }

}