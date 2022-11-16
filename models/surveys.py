from pydantic import BaseModel
from datetime import datetime

class Survey(BaseModel):
    nombre : str
    correo : str
    edad : int
    sexo : str
    estado_civil : str
    habla_lengua_indigena : str
    cual_lengua_indigena : str | None = None
    ingresos_mensuales_hogar : str
    viven_misma_vivienda : str
    cuantas_personas_trabajan : int
    principal_ingreso_economico : str
    sector_economico : str
    horas_laborales : int
    minutos_llegar_trabajo : int
    cantidad_menores_femenino: int | None = None
    cantidad_menores_masculino: int | None = None
    quien_cuida_menores: str | None = None
    menores_asisten_escuela: int | None = None
    rango_edad_menores: str | None = None
    servicio_medico: str
    lugar_residencia: str
    ultimo_grado_estudios_principal_ingreso: str
    ultimo_grado_estudios_encuestado: str
    principales_necesidades: str
    cual_principal_necesidad: str
    conoce_ciam: str
    actividades_recomendadas: str
    hora_encuesta: datetime
