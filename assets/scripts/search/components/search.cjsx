React = window.React
State = require '../state'

Search = React.createClass

    mixins: [State.mixin]

    cursors:
        query: ['filter', 'query']

    render: () ->
        <input type="text" placeholder="Search" value={@cursors.query.get()} onChange={@handleChange} />

    handleChange: (e) ->
        @cursors.query.edit(e.target.value)

module.exports = Search
