using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace cooking
{
    public partial class Type_user : Form
    {
        public Type_user()
        {
            InitializeComponent();
        }

        private void type_userBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.type_userBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.food);

        }

        private void Type_user_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'food.type_user' table. You can move, or remove it, as needed.
            this.type_userTableAdapter.Fill(this.food.type_user);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            type_userBindingNavigatorSaveItem_Click(sender, e);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            type_userBindingSource.AddNew();
            type_userBindingSource.MoveLast();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            type_userBindingSource.RemoveCurrent();
            type_userBindingNavigatorSaveItem_Click(sender, e);

        }
    }
}
