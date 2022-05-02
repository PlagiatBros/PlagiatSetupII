var EDIT_QUEUE = {}
var CLIENTS = {}

function send_mentat(address, ...args){
    send(...settings.read('send')[0].split(':'), address, ...args)
}

app.on('open', (data, client)=>{
    send_mentat('/OpenStageControl', 'session_loaded', 0)
})

app.on('sessionOpened', (data, client)=>{
    send_mentat('/OpenStageControl', 'session_loaded', 1)
    //for (var k in EDIT_QUEUE) {
    //    receive('/EDIT', k, EDIT_QUEUE[k], {clientId: client.id})
    //}
})

module.exports = {

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
