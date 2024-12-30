from odoo import api, fields, models

class BlueShepherdTour(models.Model):
    _name = 'blue.shepherd.tour'
    _description = 'Onboarding Tour'
    _order = 'sequence, id'

    name = fields.Char(required=True, translate=True)
    description = fields.Text(translate=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    
    # Tour configuration
    modal_overlay = fields.Boolean(
        string='Show Modal Overlay',
        default=True,
        help='Show a dark overlay behind the shepherd elements'
    )
    default_step_options = fields.Text(
        string='Default Step Options',
        help='JSON configuration for default step options'
    )
    exit_on_escape = fields.Boolean(
        string='Exit on Escape',
        default=True,
        help='Allow closing the tour with ESC key'
    )
    keyboard_navigation = fields.Boolean(
        string='Keyboard Navigation',
        default=True,
        help='Allow navigation with arrow keys'
    )
    
    # Steps relationship
    step_ids = fields.One2many(
        'blue.shepherd.step',
        'tour_id',
        string='Tour Steps'
    )
    step_count = fields.Integer(
        compute='_compute_step_count',
        store=True
    )
    
    # Trigger configuration
    trigger_on = fields.Selection([
        ('manual', 'Manual'),
        ('page_load', 'Page Load'),
        ('element_present', 'Element Present'),
        ('action', 'After Action')
    ], default='manual', required=True)
    trigger_page = fields.Char(
        string='Trigger Page',
        help='URL path that triggers the tour'
    )
    trigger_element = fields.Char(
        string='Trigger Element',
        help='CSS selector for the element that triggers the tour'
    )
    trigger_action_id = fields.Many2one(
        'ir.actions.actions',
        string='Trigger Action'
    )
    
    @api.depends('step_ids')
    def _compute_step_count(self):
        for tour in self:
            tour.step_count = len(tour.step_ids)