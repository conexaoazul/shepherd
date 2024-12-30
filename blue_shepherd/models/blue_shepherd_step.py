from odoo import api, fields, models

class BlueShepherdStep(models.Model):
    _name = 'blue.shepherd.step'
    _description = 'Tour Step'
    _order = 'sequence, id'

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(default=10)
    tour_id = fields.Many2one(
        'blue.shepherd.tour',
        string='Tour',
        required=True,
        ondelete='cascade'
    )
    
    # Step content
    title = fields.Char(translate=True)
    text = fields.Html(translate=True)
    
    # Step positioning
    element = fields.Char(
        string='Target Element',
        help='CSS selector for the element to attach the step to'
    )
    position = fields.Selection([
        ('auto', 'Auto'),
        ('top', 'Top'),
        ('top-start', 'Top Start'),
        ('top-end', 'Top End'),
        ('bottom', 'Bottom'),
        ('bottom-start', 'Bottom Start'),
        ('bottom-end', 'Bottom End'),
        ('right', 'Right'),
        ('right-start', 'Right Start'),
        ('right-end', 'Right End'),
        ('left', 'Left'),
        ('left-start', 'Left Start'),
        ('left-end', 'Left End'),
    ], default='auto', required=True)
    
    # Step behavior
    scrollTo = fields.Boolean(
        string='Scroll to Element',
        default=True,
        help='Automatically scroll to the element'
    )
    modalOverlayOpeningPadding = fields.Integer(
        string='Overlay Padding',
        default=0,
        help='Padding between the element and overlay highlight'
    )
    
    # Buttons configuration
    show_cancel_link = fields.Boolean(
        string='Show Cancel Button',
        default=True
    )
    cancel_text = fields.Char(
        string='Cancel Button Text',
        default='Skip',
        translate=True
    )
    next_text = fields.Char(
        string='Next Button Text',
        default='Next',
        translate=True
    )
    back_text = fields.Char(
        string='Back Button Text',
        default='Back',
        translate=True
    )
    
    # Advanced options
    extra_options = fields.Text(
        string='Extra Options',
        help='Additional JSON configuration for this step'
    )