

function ControlButton(name, properties){
	ControlBase.call(this, name, properties);
};
ControlButton.prototype = Object.create(ControlBase.prototype);


////////////////////////////////////////////////////////////////////////////////

ControlButton.prototype.init_control = function(){
	var html = "<div class='field ControlButton' ><label>&nbsp;</label>";
	html +="<button title='"+this.properties.help+"' id='"+this.control_id()+"' class='ui button' >";
	html += this.properties.label;
	html += '</button>';
	html += '</div>';
	
	this.jquery_place().replaceWith(html);

	var self = this;
	this.jquery().click(function(){
		self.basewidget.fire_event( self.name, 'pressed' )
	});
};

////////////////////////////////////////////////////////////////////////////////