from rolepermissions.roles import AbstractUserRole

class MedicoRol(AbstractUserRole):
	available_permissions = {
        'medicos': True,
    }
class PacienteRol(AbstractUserRole):
	available_permissions = {
        'pacientes': True,
    }