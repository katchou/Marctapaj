from django.forms import ModelForm
from marctapaj.models import Category

class CategoryForm(ModelForm):
	class Meta:
		model: Categoryfields = ['name']
