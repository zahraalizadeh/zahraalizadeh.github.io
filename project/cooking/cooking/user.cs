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
    public partial class user : Form
    {
        public user()
        {
            InitializeComponent();
        }

        private void userBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.userBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.food);

        }

        private void user_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'food.type_user' table. You can move, or remove it, as needed.
            this.type_userTableAdapter.Fill(this.food.type_user);
            // TODO: This line of code loads data into the 'food.user' table. You can move, or remove it, as needed.
            this.userTableAdapter.Fill(this.food.user);

        }
    }
}
