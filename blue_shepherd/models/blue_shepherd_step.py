from odoo import api, fields, models

class BlueShepherdStep(models.Model):
    _name = 'blue.shepherd.step'
    _description = 'Passo do Tour'
    _order = 'sequence, id'

    name = fields.Char('Nome', required=True, translate=True)
    sequence = fields.Integer('Sequência', default=10)
    tour_id = fields.Many2one(
        'blue.shepherd.tour',
        string='Tour',
        required=True,
        ondelete='cascade'
    )
    
    # Step content
    title = fields.Char('Título', translate=True)
    text = fields.Html('Conteúdo', translate=True)
    
    # Step positioning
    element = fields.Char(
        string='Elemento Alvo',
        help='Seletor CSS para o elemento ao qual o passo será anexado'
    )
    position = fields.Selection([
        ('auto', 'Automático'),
        ('top', 'Topo'),
        ('top-start', 'Topo Início'),
        ('top-end', 'Topo Fim'),
        ('bottom', 'Base'),
        ('bottom-start', 'Base Início'),
        ('bottom-end', 'Base Fim'),
        ('right', 'Direita'),
        ('right-start', 'Direita Início'),
        ('right-end', 'Direita Fim'),
        ('left', 'Esquerda'),
        ('left-start', 'Esquerda Início'),
        ('left-end', 'Esquerda Fim'),
    ], string='Posição', default='auto', required=True)
    
    # Step behavior
    scrollTo = fields.Boolean(
        string='Rolar até o Elemento',
        default=True,
        help='Rola automaticamente até o elemento'
    )
    modalOverlayOpeningPadding = fields.Integer(
        string='Padding do Overlay',
        default=0,
        help='Espaçamento entre o elemento e o destaque do overlay'
    )
    
    # Buttons configuration
    show_cancel_link = fields.Boolean(
        string='Mostrar Botão Cancelar',
        default=True
    )
    cancel_text = fields.Char(
        string='Texto do Botão Cancelar',
        default='Pular',
        translate=True
    )
    next_text = fields.Char(
        string='Texto do Botão Próximo',
        default='Próximo',
        translate=True
    )
    back_text = fields.Char(
        string='Texto do Botão Voltar',
        default='Voltar',
        translate=True
    )
    
    # Advanced options
    extra_options = fields.Text(
        string='Opções Extras',
        help='Configuração JSON adicional para este passo'
    )