from odoo import api, fields, models

class BlueShepherdTour(models.Model):
    _name = 'blue.shepherd.tour'
    _description = 'Tour de Onboarding'
    _order = 'sequence, id'

    name = fields.Char('Nome', required=True, translate=True)
    description = fields.Text('Descrição', translate=True)
    sequence = fields.Integer('Sequência', default=10)
    active = fields.Boolean('Ativo', default=True)
    
    # Tour configuration
    modal_overlay = fields.Boolean(
        string='Mostrar Overlay Modal',
        default=True,
        help='Mostra um overlay escuro atrás dos elementos do tour'
    )
    default_step_options = fields.Text(
        string='Opções Padrão dos Passos',
        help='Configuração JSON para opções padrão dos passos'
    )
    exit_on_escape = fields.Boolean(
        string='Sair com ESC',
        default=True,
        help='Permite fechar o tour com a tecla ESC'
    )
    keyboard_navigation = fields.Boolean(
        string='Navegação por Teclado',
        default=True,
        help='Permite navegação com as teclas de seta'
    )
    
    # Steps relationship
    step_ids = fields.One2many(
        'blue.shepherd.step',
        'tour_id',
        string='Passos do Tour'
    )
    step_count = fields.Integer(
        string='Quantidade de Passos',
        compute='_compute_step_count',
        store=True
    )
    
    # Trigger configuration
    trigger_on = fields.Selection([
        ('manual', 'Manual'),
        ('page_load', 'Carregamento da Página'),
        ('element_present', 'Elemento Presente'),
        ('action', 'Após Ação')
    ], string='Acionar Em', default='manual', required=True)
    trigger_page = fields.Char(
        string='Página de Acionamento',
        help='Caminho URL que aciona o tour'
    )
    trigger_element = fields.Char(
        string='Elemento de Acionamento',
        help='Seletor CSS para o elemento que aciona o tour'
    )
    trigger_action_id = fields.Many2one(
        'ir.actions.actions',
        string='Ação de Acionamento'
    )
    
    @api.depends('step_ids')
    def _compute_step_count(self):
        for tour in self:
            tour.step_count = len(tour.step_ids)