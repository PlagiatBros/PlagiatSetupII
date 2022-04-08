var EDIT_QUEUE = {}

app.on('sessionOpened', (data, client)=>{
    for (var k in EDIT_QUEUE) {
        receive('/EDIT', data.args[0].value, EDIT_QUEUE[k], {clientId: client.id})
    }
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
            receive('/EDIT', data.args[0].value, EDIT_QUEUE[data.args[0].value])
            return
        }

        return data

    }

}
