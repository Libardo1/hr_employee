from openerp.osv import fields,orm
from openerp.tools.translate import _
from datetime import datetime,date
import time

class hr_employee(orm.Model):
	_name = "hr.employee"
	_inherit = "hr.employee"

	def compute_age(self,cr,uid,ids,field_name,arg,context=None):
		result = {}
		age = 0
		for rec in self.browse(cr,uid,ids,context=context):
			if rec.birthdate:
				get_birthdate = datetime.strptime(rec.birthdate,'%Y-%m-%d')
				year_of_birth = int(get_birthdate.strftime("%Y"))
				current_year = datetime.now().year 
				age = current_year - year_of_birth
			result[rec.id] = str(age)
			return result

	_columns = {
		'work_number' : fields.char("Work Number"),
		'employee_status' : fields.selection([('working','Working'),('left','Left')],"Status"),
		'entry_date' : fields.date("Entry Date"),
		'id_number' : fields.char("ID Card Number"),
		'horn_gender' : fields.selection([('male','Male'),('female','Female')],'Gender'),
		'internal_number' : fields.char('Internal Number'),
		'id_address' : fields.char("ID Address"),
		'graduation_date' : fields.date("Graduation Date"),
		'graduated_school' : fields.char("Graduated School"),
		'major' : fields.char("Major"),
		'nation' : fields.char("Nation"),
		'id_ending_date' : fields.date("ID Ending Date"),
		'marital_status' : fields.selection([('not married','Not Married'),('married','Married')],"Marital Status"),
		'degree' : fields.many2one('hr.recruitment.degree',"Degree"),
		'hometown' : fields.char("Hometown"),
		'leave_date' : fields.date("Leave Date"),
		'promotion_date' : fields.date("Promotion Date"),
		'leave_reason' : fields.char("Leave Reason"),
		'leave_type' : fields.char("Leave Type"),
		'import_number' : fields.char("Import Number"),
		'work_age' : fields.char("Work Age"),
		'age' : fields.function(compute_age,type='char',string="Age"),
		'political_status' : fields.char("Political Status"),
		'emergency_contact' : fields.char("Emergency Contact"),
		'contact_number' : fields.char("Contact Number"),
		'star_evaluation' : fields.char("Star Evaluation"),
		'birthdate' : fields.date("Birthdate"),
	}