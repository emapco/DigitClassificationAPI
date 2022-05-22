import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/upload',
      name: 'upload',
      component: () => import('../views/UploadView.vue')
    },
    {
      path: '/draw',
      name: 'draw',
      component: () => import('../views/DrawView.vue')
    },
    {
      path: '/:catchAll(.*)',
      redirect: '/draw'
    }
  ]
})

export default router
