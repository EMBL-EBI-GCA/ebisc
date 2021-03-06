classNames = require 'classnames'

DropdownMultiSelect = React.createClass

    getInitialState: () ->
        showMenu: false

    showMenu: () ->
        @setState showMenu: true
        window.addEventListener('click', @hideMenu, true)

    hideMenu: (e) ->

        if e.target == $('.dropdown-button', @getDOMNode())[0]

            e.stopPropagation()

            @setState showMenu: false
            window.removeEventListener('click', @hideMenu, true)

        else if not $(@getDOMNode()).has($(e.target)).length

            @setState showMenu: false
            window.removeEventListener('click', @hideMenu, true)

    componentWillUnmount: () ->
        window.removeEventListener('click', @hideMenu, true)

    render: () ->
        <div className={classNames('dropdown': true, 'two-cols': @props.items.length >= 15, 'has-selection': @props.hasSelection)}>
            <div className="dropdown-container">
                <div className="dropdown-button" onClick={@showMenu}>{@props.label}</div>
                <ul className={classNames('dropdown-menu': true, 'checkbox': true, 'show-menu': @state.showMenu)}>
                {(<Item key={item.name} item={item} action=@props.action /> for item in @props.items)}
                </ul>
            </div>
        </div>

Item = React.createClass

    handleOnClick: () ->
        @props.action(@props.item.name, not @props.item.selected)

    render: () ->
        <li onClick={@handleOnClick} className={classNames(selected: @props.item.selected != undefined and @props.item.selected or false)}>
            <div className="checkbox"></div>
            <label>{@props.item.label}</label>
        </li>

module.exports = DropdownMultiSelect
