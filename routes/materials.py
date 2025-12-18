from flask import Blueprint, render_template, redirect, url_for, send_from_directory, flash, current_app
from extensions import db
from models.material import Material
import os

materials_bp = Blueprint('materials', __name__, url_prefix='/materials')

@materials_bp.route('/')
def list_materials():
    materials = Material.query.all()
    return render_template('materials/list.html', materials=materials)

@materials_bp.route('/<int:material_id>')
def material_detail(material_id):
    material = Material.query.get_or_404(material_id)
    return render_template('materials/detail.html', material=material)

@materials_bp.route('/download/<int:material_id>', methods=['GET'])
def download_material(material_id):
    material = Material.query.get_or_404(material_id)

    directory = os.path.join(current_app.root_path, 'static', 'materials')
    filename = material.file_path

    full_path = os.path.join(current_app.root_path, 'static', 'materials', material.file_path)

    if not os.path.exists(full_path):
        flash('File not found.')
        return redirect(url_for('materials.list_materials'))
    
    return send_from_directory(directory, filename, as_attachment=True)