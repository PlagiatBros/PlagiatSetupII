var EDIT_QUEUE = {}
var CLIENTS = {}

function send_mentat(address, ...args){
    send(...settings.read('send')[0].split(':'), address, ...args)
}

app.on('open', (data, client)=>{
    // send_mentat('/OpenStageControl', 'session_loaded', 0)
})

app.on('sessionOpened', (data, client)=>{

    if (data.path.includes('hub.json')) {
        if (client.id == 'nano') {
            receive('/SESSION/OPEN', __dirname + '/nano.json', {clientId: client.id})
        } else if (client.id == 'regie') {
            receive('/SESSION/OPEN', __dirname + '/regie.json', {clientId: client.id})
        } else if (client.id == 'main') {
            receive('/SESSION/OPEN', __dirname + '/main.json', {clientId: client.id})
        }
    } else {
        send_mentat('/OpenStageControl/call', 'send_state')
    }
})

module.exports = {

    oscOutFilter: function(data) {

        if (data.address == '/LOAD') {
            return receive('/SESSION/OPEN', __dirname + '/' + data.args[0].value + '.json', {clientId: data.clientId})
        }

        return data

    },

    oscInFilter: function(data) {
        if (data.address === '/EDIT_QUEUE/START') {
            EDIT_QUEUE[data.args[0].value] = ''
            return
        }
        if (data.address === '/EDIT_QUEUE/APPEND') {
            EDIT_QUEUE[data.args[0].value] += data.args[1].value
            return
        }
        if (data.address === '/EDIT_QUEUE/END') {
            receive('/EDIT', data.args[0].value, EDIT_QUEUE[data.args[0].value], {noWarning: true})
            return
        }

        return data

    }

}
